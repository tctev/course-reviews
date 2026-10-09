# KTH Course Reviews

Flask + SQLite app for anonymous KTH course reviews, used for our DevOps course project.

## How it works

- CI (every PR, GitHub-hosted runner): Ruff, pytest, Docker build, CodeQL. `main` is protected and needs `test` to pass.
- CD (merge to `main`): builds the image tagged with the commit SHA, pushes it to GHCR, then our self-hosted runner runs `terraform apply` and a smoke test.
- Terraform (`terraform/main.tf`): the container, network and the volume where SQLite keeps the reviews.
- Dependabot keeps pip, Actions, Docker and Terraform dependencies updated.

## Run locally

```bash
pip install -r requirements-dev.txt
pytest

docker build -t course-reviews:local .
cd terraform && terraform init && terraform apply
```

Then open http://localhost:8000

## Self-hosting

The deploy runs on a self-hosted runner, so it can be any Linux machine you control. We use an Azure VM so the runner doesn't have to sit on our own laptops.

The machine needs Docker (runner user in the `docker` group), `curl`, port 8000 open and the GitHub runner installed as a service. Terraform state is kept in `$HOME/course-reviews.tfstate` on it.

## Limitations

- One machine and SQLite, so no scaling or failover.
- Terraform state is a local file, no locking or backups.
- Plain HTTP, no HTTPS.
