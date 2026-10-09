# AI-Assisted Development

AI-assisted tools were used during the development of this project as support for design discussions, documentation, troubleshooting, and review.

The team remained responsible for all technical decisions and manually reviewed and executed the suggested changes.

## Usage

| Area | How AI was used | Human verification |
|---|---|---|
| Architecture and design | Discussed the CI/CD architecture, Terraform setup, self-hosted runner, persistent SQLite volume, and project trade-offs. | The proposed design was reviewed by the team before implementation and compared with the project requirements. |
| Documentation | Helped structure and review the project README, including the architecture description, deployment flow, limitations, and Mermaid diagram. | The documentation was manually reviewed before being committed and merged through a pull request. |
| CI/CD improvements | Suggested adding a deployment test to the GitHub Actions workflows. | Changes were reviewed through Git diffs and submitted through pull requests. CI runs were used to validate the workflow changes. |
| Troubleshooting | Helped analyze GitHub Actions behavior | Using the actual GitHub Actions job status and logs. |
| Project review | Helped compare the implementation against the KTH DevOps project grading criteria and identify missing documentation and reproducibility improvements. | The team reviewed the recommendations and decided which changes were appropriate for the scope of the project. |

## Verification and Responsibility

AI-generated suggestions were not applied automatically.

All commands, configuration changes, and documentation were reviewed by a team member before being committed. Changes to the repository were submitted through the normal pull request and CI process.

The AI assistant did not have autonomous access to the deployment machine or make deployment decisions on behalf of the team.

## Limitations

AI suggestions can be incomplete or incorrect. For example, a smoke-test command initially assumed that `curl` was installed on the self-hosted runner. The resulting deployment failure was investigated using the actual job logs before deciding how to correct the environment.

For this reason, AI output was treated as a suggestion rather than as an authoritative source.
