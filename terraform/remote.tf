terraform {
  backend "s3" {
    bucket         = "yongfeng-shared-infra-dev-terraform-remote-state"
    key            = "ymo/prti_automation/terraform.tfstate"
    region         = "us-west-2"
    # TODO: probably need to override this on terraform init calls for use in dev/qa/prod accounts?
    dynamodb_table = "shared-infrastrucutre-terraform-lock-table"
  }
}
