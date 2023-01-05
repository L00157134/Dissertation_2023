terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "eu-west-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0fe0b2cf0e1f25c8a"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}

resource "aws_instance" "Web_Server" {
  ami           = "ami-0fe0b2cf0e1f25c8a"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleWebsServerInstance"
  }
}

terraform {
  backend "s3" {
    bucket = "terraform-sate-lock-rosh"
    key    = "terrform-state-fles/terraform.tfstate"
    region = "eu-west-1"
  }
}

