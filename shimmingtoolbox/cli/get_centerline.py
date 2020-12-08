#!/usr/bin/env python3

import click
import os
import subprocess

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS,
               help="This function extracts the spinal cord centerline. Three methods are available: 'optic' "
                    "(automatic), 'viewer' (manual), and 'fitseg' (applied on segmented image). These functions output"
                    " (i) a NIFTI file with labels corresponding to the discrete centerline, and (ii) a csv file "
                    "containing the float (more precise) coordinates of the centerline in the RPI orientation.")
@click.option('-input', 'fname_input', type=click.Path(), required=True, help="(str): Input image. Example: t1.nii.gz")
@click.option('-contrast', type=click.Choice(['t1', 't2', 't2s', 'dwi']), default='t1',
              help="(str): Type of image contrast. Only with method=optic. (default: t1)")
@click.option('-method', type=click.Choice(['optic', 'fitseg']), default='optic',
              help="(str): Method used for extracting the centerline: "
                   "- optic: automatic spinal cord detection method"
                   "- fitseg: fit a regularized centerline on an already-existing cord segmentation. It will "
                   "interpolate if slices are missing and extrapolate beyond the segmentation boundaries (i.e., every "
                   "axial slice will exhibit a centerline pixel). (default: optic)")
@click.option('-centerline_algo', type=click.Choice(['polyfit', 'bspline', 'linear', 'nurbs']), default='bspline',
              help="(str): Algorithm for centerline fitting. Only relevant with -method fitseg (default: bspline)")
@click.option('-centerline_smooth', default=30, help="(int): Degree of smoothing for centerline fitting. Only for "
                                                     "-centerline-algo {bspline, linear}. (default: 30)")
@click.option('-output', type=click.Path(), default=os.path.join(os.curdir, 'mask_centerline'),
              help="(str): File name (without extension) for the centerline output files. Example: 'centerline_optic'. "
                   "(default: (os.curdir, 'mask_centerline')).")
def get_centerline_cli(fname_input, contrast, method, centerline_algo, centerline_smooth, output):
    if method == "optic":
        subprocess.run(['sct_get_centerline', '-i', fname_input, '-c', contrast, '-o', output], check=True)

    elif method == "fitseg" and (centerline_algo == "polyfit" or centerline_algo == "nurbs"):
        subprocess.run(['sct_get_centerline', '-i', fname_input, '-method', method, '-centerline-algo', centerline_algo,
                        '-o', output], check=True)

    elif method == "fitseg" and (centerline_algo == "bspline" or centerline_algo == "linear"):
        subprocess.run(['sct_get_centerline', '-i', fname_input, '-method', method, '-centerline-algo', centerline_algo,
                        '-centerline-smooth', centerline_smooth, '-o', output], check=True)

    else:
        raise ValueError("The implementation of get_centerline_cli is bad. Run get_centerline_cli -h for more "
                         "information on how to call this command.")

    click.echo(f"The path for the output mask is: {os.path.abspath(output+ '.nii.gz')}")
    return output + '.nii.gz'
