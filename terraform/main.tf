terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 4.6"
    }
  }
  # path set with -backend-config in CD, defaults to ./terraform.tfstate locally
  backend "local" {}
}

variable "image" {
  type    = string
  default = "course-reviews:local"
}

resource "docker_network" "app" {
  name = "course-reviews"
}

resource "docker_volume" "db" {
  name = "course-reviews-db"
}

resource "docker_image" "app" {
  name         = var.image
  keep_locally = true
}

resource "docker_container" "app" {
  name    = "course-reviews"
  image   = docker_image.app.image_id
  restart = "unless-stopped"

  networks_advanced {
    name = docker_network.app.name
  }

  ports {
    internal = 8000
    external = 8000
  }

  volumes {
    volume_name    = docker_volume.db.name
    container_path = "/data"
  }
}
