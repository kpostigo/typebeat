variable "ami_id" {
  type        = string
  default     = "ami-0866a3c8686eaeeba"
  description = "ubuntu 24.04 lts x86_64"
}

variable "key_name" {
  type        = string
  description = "key pair name"
}