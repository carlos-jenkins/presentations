#!/usr/bin/env python3

from pathlib import Path
from os.path import relpath
from subprocess import check_call
from shutil import which, copytree, rmtree


THEME = 'hauntr'
INPUT = 'presentations'
OUTPUT = 'presentations'


def main():
    rst2s5 = which('rst2s5.py')
    assert rst2s5, 'rst2s5.py not found!'

    rst2html5 = which('rst2html5.py')
    assert rst2html5, 'rst2html5.py not found!'

    root = Path(__file__).resolve().parent
    outdir = Path(Path.cwd() / OUTPUT)

    print('Creating output directory {} ...'.format(outdir))
    outdir.mkdir(parents=True, exist_ok=True)

    # Render index
    index_input = root / INPUT / 'index.rst'
    index_output = outdir / 'index.html'
    print('Rendering index {} to {} ...'.format(
        index_input,
        index_output,
    ))
    check_call([
        rst2html5,
        '--syntax-highlight', 'short',
        '--stylesheet', '',
        str(index_input),
        str(index_output)
    ])

    # Copy theme
    theme_indir = root / 'themes' / THEME
    assert theme_indir.is_dir(), 'No theme {}'.format(THEME)

    theme_outdir = outdir / 'themes' / THEME
    if theme_outdir.is_dir():
        rmtree(str(theme_outdir))

    print('Copying theme {} ...'.format(THEME))
    copytree(str(theme_indir), str(theme_outdir))

    # Render presentations
    for presentation in root.glob(INPUT + '/*/*.rst'):

        # Output directory
        output = outdir / presentation.parent.name
        output.mkdir(parents=True, exist_ok=True)

        # Render in HTML
        print('Processing {} ...'.format(presentation))
        print('        -> Output {}'.format(output))

        check_call([
            rst2s5,
            '--syntax-highlight', 'short',
            '--stylesheet', '',
            '--theme-url', THEME,
            str(presentation),
            str(output / 'index.html')
        ])

        # Copy images
        images = presentation.parent / 'images'
        if images.is_dir():
            images_outdir = output / 'images'

            if images_outdir.is_dir():
                rmtree(str(images_outdir))

            print('        -> Copying images to {} ...'.format(images_outdir))
            copytree(str(images), str(images_outdir))
        else:
            print('        -> No images to copy.')

        # Link theme
        relative_theme = relpath(str(theme_outdir), str(output))
        print('        -> Linking {} theme as {} ...'.format(
            THEME, relative_theme
        ))
        check_call([
            'ln',
            '--symbolic',
            '--force',
            relative_theme,
            str(output / THEME),
        ])


if __name__ == '__main__':
    main()
