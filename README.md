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
  --port 61309 \
  --reload --autoreload-port 61310 \
  app.py
```

## 3.3 Contribution

```bash
git pull

git add .
git commit -m "your message"
git push
```

# 4. References

- [**Shiny**: https://shiny.posit.co/py/](https://shiny.posit.co/py/)
- [**Stereopy**: https://stereopy.readthedocs.io/en/latest/](https://stereopy.readthedocs.io/en/latest/)
