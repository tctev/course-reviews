# AI usage

We used an AI assistant in this project, mostly for proofreading our documentation, for finding the right documentation of the libraries and tools we used, and as help when something broke. The final code, workflows and Terraform configuration were written and decided by us. We are responsible for everything in this repository and we can explain all parts of it.

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

Since most of these libraries and tools were new to us, we also asked the assistant about implementation on different occasions, for example how a function could be written or what different ways there are to implement something. We used the answers to understand the options, then picked the approach that fit our project and adapted it ourselves.

## Troubleshooting

When a CI or deployment job failed, we pasted the error from the GitHub Actions logs to the assistant and used the answer as a starting point. Before changing anything we checked the real cause ourselves in the job logs. Every fix was done in a pull request and had to pass CI before merging.

## How we checked the output

Nothing the assistant suggested was applied automatically. A team member reviewed every command, configuration change and piece of documentation before it was committed, and all changes went through the normal pull request and CI process. The assistant had no access to the deployment machine and did not make any deployment decisions for us.

AI answers can be incomplete or just wrong, so we treated them as suggestions and not as a reliable source.
