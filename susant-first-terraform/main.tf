terraform {
    required_version = ">= 1.9.0"
    required_providers {
      aws = {
        source = "hasicorp/aws"
        version = "~>6.27"
      }
      random = {
        source = "hashicorp/random"
        version = "~>3.7.3"
      }
    }
}

provider " aws" {
    region = "us-east-1"
}

resource "random_id" "bucket_suffix" {
    byte_length = 6
}

resource "aws_s3_bucket" "my_bucket" {
    bucket = "my-first-bucket-${random_id.bucket_suffix.hex}"
    }

output "bucket_name" {
    value = aws_s3_bucket.my_bucket.bucket
}