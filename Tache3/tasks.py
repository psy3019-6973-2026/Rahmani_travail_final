import os
import requests
from pathlib import Path
from invoke import task
from airoh.containers import docker_run, docker_build, docker_archive, docker_setup

@task
def setup(c):
    """
    Setup all the requirements.
    """
    from airoh.utils import setup_env_python
    setup_env_python(c, "requirements.txt")
    print(f"✨ Setup complete!")

@task(
    help={
        "name": "Nom logique du fichier, tel que défini dans la section 'files' de invoke.yaml."
    }
)
def import_file(c, name):
    """🌐 Download a single file from a URL using urllib."""
    from urllib.request import Request, urlopen
    
    files = c.config.get("files", {})
    if name not in files:
        raise ValueError(f"❌ No file config found for '{name}' in invoke.yaml.")

    entry = files[name]
    url = entry.get("url")
    output_file = entry.get("output_file")

    if not url or not output_file:
        raise ValueError(
            f"❌ Entry for '{name}' must define both 'url' and 'output_file'."
        )

    output_path = Path(output_file)
    tmp_path = output_path.with_suffix(output_path.suffix + ".part")

    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"🫧 Skipping {name}: {output_file} already exists.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path.unlink(missing_ok=True)

    print(f"📥 Downloading '{name}' from {url}")
    print(f"📁 Target: {output_file}")

    req = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15'}
    )

    try:
        with urlopen(req, timeout=60) as response, tmp_path.open("wb") as f:
            total = 0
            while True:
                chunk = response.read(8192)
                if not chunk:
                    break
                f.write(chunk)
                total += len(chunk)

        if total == 0:
            tmp_path.unlink(missing_ok=True)
            raise RuntimeError(f"❌ Downloaded 0 bytes for '{name}'.")

        tmp_path.replace(output_path)

    except Exception as e:
        tmp_path.unlink(missing_ok=True)
        raise RuntimeError(f"❌ Failed to download '{name}' from {url}: {e}") from e

    print(f"✅ Downloaded {name} to {output_file} ({output_path.stat().st_size} bytes)")

@task
def fetch(c):
    url = "https://zenodo.org/api/records/8275363"
    out_dir = c.config.source_data_dir

    os.makedirs(out_dir, exist_ok=True)

    print("📥 Fetching dataset metadata...")
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()

    files = data["files"]

    for f in files:
        filename = f["key"]
        download_url = f["links"]["self"]
        size_mb = f["size"] / 1e6

        output_path = os.path.join(out_dir, filename)

        if os.path.exists(output_path):
            print(f"⏭️ Skipping {filename}")
            continue

        print(f"⬇️ {filename} ({size_mb:.1f} MB)")

        with requests.get(download_url, stream=True) as resp:
            resp.raise_for_status()
            with open(output_path, "wb") as out:
                for chunk in resp.iter_content(chunk_size=8192):
                    out.write(chunk)

    print("✅ All files downloaded")

@task
def run_simulation(c):
    """
    Run a small simulation.
    """
    output_dir = Path(c.config.get("output_data_dir"))
    from code.simulation import simulation
    simulation(output_dir)

@task(pre=[run_simulation])
def run_figure(c):
    """
    Generate figures from the simulation output using a notebook.
    """
    from airoh.utils import run_figures, ensure_dir_exist

    notebooks_dir = Path(c.config.get("notebooks_dir"))
    output_dir = Path(c.config.get("output_data_dir")).resolve()
    source_dir = Path(c.config.get("source_data_dir")).resolve()

    ensure_dir_exist(c, "output_data_dir")
    run_figures(c, notebooks_dir, output_dir, keys=["source_data_dir", "output_data_dir"])

@task(pre=[run_simulation, run_figure])
def run(c):
    print("all analyses completed")

@task
def clean(c):
    """
    Clean the output folder.
    """
    from airoh.utils import clean_folder
    clean_folder(c, "output_data_dir", "*.png")
    clean_folder(c, "output_data_dir", "*.csv")
