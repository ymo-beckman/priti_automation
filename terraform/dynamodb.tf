module "dynamodb_table_CytobankPrTiConfigUser" {
  source       = "terraform-aws-modules/dynamodb-table/aws"
  version      = "1.1.0"
  name         = "Cytobank-PrTiConfigUserTable"
  billing_mode = "PAY_PER_REQUEST"

  point_in_time_recovery_enabled = true

  hash_key = "githubLogin"
  attributes = [
    {
      name = "githubLogin"
      type = "S"
    }
  ]
}

resource "aws_ssm_parameter" "CytobankPrTiConfigUser_id" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiConfigUserTable_id"
  value     = module.dynamodb_table_CytobankPrTiConfigUser.dynamodb_table_id
  type      = "String"
  overwrite = "true"
}

resource "aws_ssm_parameter" "CytobankPrTiConfigUser_arn" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiConfigUserTable_arn"
  value     = module.dynamodb_table_CytobankPrTiConfigUser.dynamodb_table_arn
  type      = "String"
  overwrite = "true"
}

module "dynamodb_table_CytobankPrTiConfigProject" {
  source       = "terraform-aws-modules/dynamodb-table/aws"
  version      = "1.1.0"
  name         = "Cytobank-PrTiConfigProjectTable"
  billing_mode = "PAY_PER_REQUEST"

  point_in_time_recovery_enabled = true

  hash_key = "project_key"
  attributes = [
    {
      name = "project_key"
      type = "S"
    }
  ]
}

resource "aws_ssm_parameter" "CytobankPrTiConfigProject_id" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiConfigProjectTable_id"
  value     = module.dynamodb_table_CytobankPrTiConfigProject.dynamodb_table_id
  type      = "String"
  overwrite = "true"
}

resource "aws_ssm_parameter" "CytobankPrTiConfigProject_arn" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiConfigProjectTable_arn"
  value     = module.dynamodb_table_CytobankPrTiConfigProject.dynamodb_table_arn
  type      = "String"
  overwrite = "true"
}

module "dynamodb_table_CytobankPrTiCollectRecord" {
  source       = "terraform-aws-modules/dynamodb-table/aws"
  version      = "1.1.0"
  name         = "Cytobank-PrTiCollectRecordTable"
  billing_mode = "PAY_PER_REQUEST"

  point_in_time_recovery_enabled = true

  hash_key     = "record_key"
  range_key    = "review_time"

  attributes = [
    {
      name = "record_key"
      type = "S"
    },
    {
      name = "review_time"
      type = "S"
    }
  ]
}

resource "aws_ssm_parameter" "CytobankPrTiCollectRecord_id" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiCollectRecordTable_id"
  value     = module.dynamodb_table_CytobankPrTiCollectRecord.dynamodb_table_id
  type      = "String"
  overwrite = "true"
}

resource "aws_ssm_parameter" "CytobankPrTiCollectRecord_arn" {
  name      = "/prti/dev/shared-infra/dynamodb/PrTiCollectRecordTable_arn"
  value     = module.dynamodb_table_CytobankPrTiCollectRecord.dynamodb_table_arn
  type      = "String"
  overwrite = "true"
}
