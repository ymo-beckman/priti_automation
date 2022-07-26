provider "aws" {
  region = var.aws_region
  // lambda support image required aws provider version >= 3.19
  // lambda support ephemeral_storage required aws provider version >= 4.8.0
  version = ">= 4.8.0"
}
