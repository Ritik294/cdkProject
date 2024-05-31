#!/usr/bin/env python3
import os

from aws_cdk import App, Stack

from infra.infra_stack import InfraStack


app = App()
InfraStack(app, "Bankingappstack")

app.synth()
