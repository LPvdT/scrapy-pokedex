from .factory import command_factory

scrape = command_factory("scrape", "cwd")
types = command_factory("gen_types")
setup_precommit = command_factory("setup_precommit")
precommit = command_factory("precommit")
