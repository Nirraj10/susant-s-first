terraform {
  required_version = "~.1.0"
  required_providers {
    aws = {
        source = "hasicorp/aws"
        version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

provider "aws" {
  region = "eu-west-1"
  alias = eu-west
}

resource "aws_s3_bucket" "my_bucket" {
    bucket = "my-first-989"
}
resource "aws_s3_bucket" "bucket_eu_west_1" {
    bucket = "my-second-333"
    provider = aws.eu-west
}