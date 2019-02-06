#  -*- coding: utf-8 -*-
#    @package: diff.py
#     @author: Guilherme N. Ramos (gnramos@unb.br)
# @disciplina: Algoritmos e Programação de Computadores
#
# Mostra os arquivos.


from argparse import ArgumentParser
import os
import subprocess


def project_dir(project_dir):
    u"""Verifica o diretório do projeto."""
    if not os.path.exists(project_dir):
        raise ValueError('"{}" não é um diretório válido.'.format(project_dir))
    return project_dir


def parse_args():
    """Processa os argumentos fornecidos."""
    ap = ArgumentParser(description='Apresenta a evolução do código de um '
                                    'projeto.')
    ap.add_argument('projeto', type=project_dir,
                    help='Nome do projeto cujos arquivos devem ser '
                         'processados.')
    ap.add_argument('-l', '--linguagem',
                    help='Extensão dos arquivos a processar.',
                    default='c', choices=['c', 'py'])
    return ap.parse_args()


def terminal(cmd):
    """Executa o comando dado no terminal."""
    subprocess.run('clear && {}'.format(cmd), shell=True)


def diff_files(projeto, linguagem):
    u"""Mostra a diferença entre arquivos de código do projeto.

    Itera pela lista de todos os arquivos de código do projeto, em ordem
    alfabética, e mostra a diferença entre eles com o comando diff.
    """
    if not projeto.endswith('/'):
        projeto += '/'

    files = sorted('{}{}'.format(projeto, file)
                   for file in os.listdir(projeto)
                   if file.endswith('.' + linguagem))

    if files:
        terminal('cat {}'.format(files[0]))
        input('\n [Enter] para continuar...')

        for x in range(1, len(files)):
            terminal('diff {} {}'.format(files[x - 1], files[x]))
            input('\n [Enter] para continuar ({}/{})...'.format(x, len(files)))

        terminal('cat {}'.format(files[-1]))


if __name__ == '__main__':
    args = parse_args()
    diff_files(args.projeto, args.linguagem)
