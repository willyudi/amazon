#!/usr/bin/env python
# encoding: utf-8
import csv
#Incidentes
#SAT;Serviço;Título;Solicitante;Superior Imediato;Empresa;Departamento;Sistema Afetado;Gestor do Sistema;Empresa do Sistema;Departamento do Sistema;Estado;Analista Responsável;Executor;Data de Abertura;Data de Atribuição;Data de Transferência;Data de Pedido de Parecer;Data de Retorno de Parecer;Data Efetiva de Conclusão;Coordenador;Motivo do Encerramento
#22 colunas
with open('incidentes.csv', 'r', newline='', encoding='mac_cyrillic') as csv_file:
	csv_reader = csv. reader(csv_file)
	contador = 1
	for line in csv_reader:
		print(str(contador) + ' - ' + str(line))
		contador = contador + 1
		