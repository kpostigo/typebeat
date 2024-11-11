terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_security_group" "analyzer_sg" {
  name        = "analyzer_sg"
  description = "typebeat spotify api client security group"
}

resource "aws_vpc_security_group_egress_rule" "analyzer_sg_egress" {
  description       = "Allow all outbound traffic"
  security_group_id = aws_security_group.analyzer_sg.id

  from_port   = 0
  to_port     = 0
  ip_protocol = "-1"
  cidr_ipv4   = "0.0.0.0/0"
}

resource "aws_vpc_security_group_ingress_rule" "analyzer_sg_ingress_ssh" {
  description       = "SSH"
  security_group_id = aws_security_group.analyzer_sg.id

  from_port   = 22
  to_port     = 22
  ip_protocol = "tcp"
  cidr_ipv4   = "0.0.0.0/0"
}

resource "aws_instance" "analyzer" {
  ami                    = var.ami_id
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.analyzer_sg.id]
  key_name               = var.key_name

  tags = {
    Name = "typebeat analyzer"
  }
}