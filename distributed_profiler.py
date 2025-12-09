def main(argv: Sequence[str]) -> int:
    try:
        args = parse_args(argv)
        setup_logger(args.verbose)
        try:
            args_dict = {key: getattr(args, key) for key in vars(args)}
            logging.debug("Parsed arguments: %s", args_dict)
        except Exception:
            logging.debug("Parsed arguments (unable to serialize for logging): %s", args)

        profiler = DistributedProfiler(args)
        asyncio.run(profiler.run())
    except (ConfigError, TaskError) as exc:
        logging.error("%s", exc)
        return 1
    except KeyboardInterrupt:
        logging.warning("Interrupted by user")
        return 130
    return 0
