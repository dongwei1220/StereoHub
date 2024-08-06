## 1. StereoHub

### 1.1 StereoHub Introduction:

**StereoHub: An interactive cloud platform for downstream analytics at Stereo-Seq.** The `StereoHub` user interface is designed and developed based on the `Shiny v1.0.0` framework of `Python v3.8.10`, providing rich web components for data manipulation, function parameters, and result display, making data analytics parameters as completely intuitive as possible for scientists. The functions of `StereoHub` for Stereo-Seq spatiotemics data analytics are realized by important functional modules such as `stereopy v3.1.3`, `anndata v0.9.2`, `biopython v1.83.0`, `hdf5 v1.14.0`, `panel v0.14.4`, `bokeh v2.4.3`, `plotly v5.23.0`, etc. Thanks to these excellent open-source modules.

![StereoHub UI](assets/image/StereoHub-UI.jpg)

[***a. Github Team: https://github.com/StereoHub/***](https://github.com/StereoHub/)

[***b. Source Repository: https://github.com/StereoHub/StereoHub***](https://github.com/StereoHub/StereoHub)

[***c. Documents: https://stereohub.github.io***](https://stereohub.github.io)

[***d. Cloud Platform: https://hiplot.com.cn/stereohub***](https://hiplot.com.cn/stereohub)

---

### 2.1 Stereo-Seq Technology:

[***a. STomics Stereo-Seq: https://stomics.tech***](https://stomics.tech)

[***b. STomics Cloud: https://cloud.stomics.tech***](https://cloud.stomics.tech)

[***c. STOmics Database: https://db.cngb.org/stomics/***](https://db.cngb.org/stomics/)

[***d. ImageStudio, StereoMap: https://stomics.tech/products/BioinfoTools/OfflineSoftware***](https://stomics.tech/products/BioinfoTools/OfflineSoftware)

[***e. STomics Github: https://github.com/STOmics/***](https://github.com/STOmics/)

[***f. Stereopy: https://github.com/STOmics/Stereopy/***](https://github.com/STOmics/Stereopy/)

## 2. For User

### 2.1 StereoHub Cloud `Come soon`

[StereoHub Cloud: https://stereohub.github.io/stereohub/](https://stereohub.github.io/stereohub/)

## 3. For Developer

### 3.1 Install

```bash
git clone git@github.com:StereoHub/StereoHub.git
cd StereoHub

conda env create -f stereohub.yml
conda activate stereohub
```

### 3.2 Development

```bash
# 1. For Windows
.\start-win.bat

# 2. For Linux
bash start-linux.sh

# 3. All terminals
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

### 3.3 Contribution

```bash
git pull

git add .
git commit -m "your message"
git push
```

### 3.4 Deploy: Shinylive (WebAssembly + Pyodide)
- [**Shinylive: Shiny + WebAssembly**: https://shiny.posit.co/py/docs/shinylive.html](https://shiny.posit.co/py/docs/shinylive.html)

```bash
shiny create myapp

pip install shinylive
shinylive export myapp site
python3 -m http.server --directory site 8008
```

### 3.5 Deploy: Self Host
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

## 4. References

- [**Shiny**: https://shiny.posit.co/py/](https://shiny.posit.co/py/)
- [**Stereopy**: https://stereopy.readthedocs.io/en/latest/](https://stereopy.readthedocs.io/en/latest/)
