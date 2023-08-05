import pip


def InstallRequirements(requirements_path, target_path):
    with open(requirements_path) as _:
        requirements = _.readlines()

    for requirement in requirements:
        result = pip.main([
            'install',
            '-q',
            '--platform=manylinux1_x86_64',
            f'--target={target_path}',
            '--only-binary=:all:',
            '--upgrade',
            requirement
        ])
        if result:
            pip.main(['install', '-q', f'--target={target_path}', '--upgrade', requirement])
