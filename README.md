# Experiments with the Github Container Registry

Just trying things out here, the images are based on
[`alpine`](https://hub.docker.com/_/alpine). Meow! :smile_cat:

What the [`build.yaml`](.github/workflows/build.yaml) workflow and
scripts here are supposed to do:

* Build and test a container image using Actions

* Choose suitable tags for the image (see
  [`tag-from-ref.py`](./tag-from-ref.py))

* Scan the image for vulnerabilities using
  [Trivy](https://github.com/aquasecurity/trivy-action). The scan also
  runs regularly for the `beta` and `latest` tags in the
  [`scan_images.yaml`](.github/workflows/scan_images.yaml) workflow.

* If the image should be tagged, do that and push to GHCR.

If you run the resulting image it'll meow at you, you can even give a
number of meows on the command line! :smiley_cat:

## Cleaning old images

Building and pushing an image tagged `beta` for each commit
accumulates old, now untagged beta images pretty quickly. The
[`ghcr-prune.py`](./ghcr-prune.py) script uses the [GitHub packages
API](https://docs.github.com/en/rest/reference/packages) to list image
versions, and optionally prunes untagged ones older than a given
number of days. :broom:

The [`prune_images.yaml`](.github/workflows/prune_images.yaml)
workflow uses this script to clean up once per month.
