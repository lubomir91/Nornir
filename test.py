from nornir import InitNornir
nr = InitNornir(config_file="config.yaml")


nr.config.core.num_workers
