# AI usage

We used an AI assistant in this project, mostly for proofreading our documentation, for finding the right documentation of the libraries and tools we used, and as help when something broke. The assistant also helped write parts of the code, workflows and Terraform configuration, and the design decisions were ours. We are responsible for everything in this repository and we can explain all parts of it.

## Proofreading

English is not our first language, so we asked the assistant to proofread the README and the report for spelling, grammar and sentences that were hard to understand. We also used it to go through the grading criteria of the course together with our documents and check that we cover all the project requirements (CI, CD, Infrastructure as Code, development platform, quality or security automation, a repository that can be run from the documentation, and the 2-3 page report). We went through the suggestions and kept only the ones we agreed with.

## Finding documentation

For new parts of the project we asked the assistant where to find the official documentation and which options we need. We did this for:

- Flask and Gunicorn (the app and how it runs inside the container)
- the `kreuzwerker/docker` Terraform provider (container, network and volume)
- GitHub Actions (workflow syntax, token permissions, self-hosted runners, pushing images to GHCR)
- Dependabot and CodeQL configuration
- pytest and Ruff

We always checked against the official documentation itself and did not rely only on the summary from the assistant, because sometimes it gets option names wrong or mixes up versions.

Since most of these libraries and tools were new to us, we also asked the assistant about implementation on different occasions, for example how a function could be written or what different ways there are to implement something. Some of these answers ended up in the code, after we went through them and adapted them to our project.

## Troubleshooting

When a CI or deployment job failed, we pasted the error from the GitHub Actions logs to the assistant and used the answer as a starting point. Before changing anything we checked the real cause ourselves in the job logs. Every fix to the repository was done in a pull request and had to pass CI before merging.

## How we checked the output

In some steps the assistant made changes directly, both in the repository and on the machines we used for deployment, while we followed and checked the results. Once `main` was protected, every change to the repository went through a pull request and CI.

AI answers can be incomplete or just wrong, so we treated them as suggestions and not as a reliable source.
