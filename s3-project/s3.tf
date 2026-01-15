resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "static-website" {
  bucket = "terraform-first-s3-project-${random_id.bucket_suffix.hex}"
}