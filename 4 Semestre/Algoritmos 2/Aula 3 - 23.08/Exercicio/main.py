from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

print("---- Aluno ----")
aluno = Aluno("123", "Jonatha", "ACBD123")
aluno.imprimir()

print("---- Ensino Médio ----")
ensinoMedio = AlunoEnsinoMedio("123", "Jonatha", "ACBD123", "Oitavo ano")
ensinoMedio.imprimir()

print("---- Graduação ----")
graduacao = AlunoGraduacao("123", "Jonatha", "ACBD123", "quarto semestre")
graduacao.imprimir()

