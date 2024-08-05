# 1. StereoHub

**StereoHub**: a shiny interface for Stereo-Seq analysis and visualization.

# 2. For User

## 2.1 StereoHub Cloud `Come soon`

[StereoHub Cloud: https://stereohub.github.io/stereohub/](https://stereohub.github.io/stereohub/)

# 3. For Developer

## 3.1 Install

```bash
git clone git@github.com:StereoHub/StereoHub.git
cd StereoHub

conda env create -f stereohub.yml
conda activate stereohub
```

## 3.2 Development

```bash
python -m shiny run \
  --host 127.0.0.1 \
  --port 5000 \
  --reload \
  --reload-includes "*.py,*.css,*.js,*.html" \
  --reload-excludes "*.png,*.pdf" \
  --log-level info \
  --app-dir "." \
  --launch-browser \
  --dev-mode \
  app.py
```

```bash
python -m shiny run --port 5000 --reload --reload-excludes "*.png,*.pdf" --launch-browser --dev-mode app.py
```

## 3.3 Contribution

```bash
git pull

git add .
git commit -m "your message"
git push
```

## 3.4 Deploy: Shinylive (WebAssembly + Pyodide)
- [**Shinylive: Shiny + WebAssembly**: https://shiny.posit.co/py/docs/shinylive.html](https://shiny.posit.co/py/docs/shinylive.html)

```bash
shiny create myapp

pip install shinylive
shinylive export myapp site
python3 -m http.server --directory site 8008
```

## 3.5 Deploy: Self Host
- [**Self-hosted deployments**: https://shiny.posit.co/py/docs/deploy-on-prem.html](https://shiny.posit.co/py/docs/deploy-on-prem.html)

```yml
# Use system python3 to run Shiny apps
python /usr/bin/python3;

# Instruct Shiny Server to run applications as the user "shiny"
run_as shiny;

# Define a server that listens on port 3838
server {
  listen 3838;

  # Define a location at the base URL
  location / {

    # Host the directory of Shiny Apps stored in this directory
    site_dir /srv/shiny-server;

    # Log all Shiny output to files in this directory
    log_dir /var/log/shiny-server;

    # When a user visits the base URL rather than a particular application,
    # an index of the applications available in this directory will be shown.
    directory_index on;
  }
}
```

# 4. References

- [**Shiny**: https://shiny.posit.co/py/](https://shiny.posit.co/py/)
- [**Stereopy**: https://stereopy.readthedocs.io/en/latest/](https://stereopy.readthedocs.io/en/latest/)
