workflow "Main Workflow" {
  on = "push"
  resolves = "SonarCloud Trigger"
}

action "SonarCloud Trigger" {
  uses = "sonarsource/sonarcloud-github-action@master"
  secrets = ["2aa3449cd734a24db158b260b00c0ea26a557ec1", "951972f29a8388a13af124ee4b4041e68c02d972"]
}

