#!/usr/bin/env python

import os
from .utils import parse_params_values
from .cli_configs import ReconstructConfig
from ...resources.processconfig import ProcessConfig
from ...app.process import WorkerProcess
from ...app.logger import Logger
from ... import version


def get_subregion(slices_indices, radio_nz):
    if len(slices_indices) == 0:
        return (0, radio_nz)
    try:
        if "-" in slices_indices:
            z_start, z_stop = slices_indices.split("-")
            z_start = int(z_start)
            z_stop = int(z_stop)
        else:
            z_idx = int(slices_indices)
            z_start = z_idx
            z_stop = z_idx + 1
    except Exception as exc:
        print("Could not interpret slice indices: %s")
        print(exc)
        exit(1)
    return (z_start, z_stop)


def main():
    args = parse_params_values(
        ReconstructConfig,
        parser_description="Perform a tomographic reconstruction.",
        program_version="nabu " + version
    )
    proc = ProcessConfig(args["input_file"])

    logger = Logger(
        "nabu",
        level=proc.nabu_config["about"]["verbosity"],
        logfile=args["log_file"]
    )

    subregion = get_subregion(
        args["slice"],
        proc.dataset_infos.radio_dims[-1]
    )
    logger.info("Going to reconstruct slices %s" % str(subregion))
    subregion = (None, None) + subregion

    # (hopefully) temporary patch
    if args["energy"] > 0:
        logger.warning("Using user-provided energy %.2f keV" % args["energy"])
        proc.dataset_infos.dataset_scanner._energy = args["energy"]
        proc.processing_options["phase"]["energy_kev"] = args["energy"]
    #

    W = WorkerProcess(
        proc,
        subregion,
        chunk_size=subregion[-1]-subregion[-2],
        logger=logger,
        extra_options={"clear_gpu_memory_after_buildsino": True}
    )
    W.process_chunk()




if __name__ == "__main__":
    main()
