from operacao import Operacao

class Menu:
    def __init__(self):
        self.opcao = -1
        self.opera = Operacao()
        self.num1 = 0
        self.num2 = 0

    def mostrarmenu(self):
        print('\n ------ MENU ------\n\n'
              + '\n0. Sair'
              + '\n1. Somar'
              + '\n2. Subtrair'
              + '\n3. Dividir'
              + '\n4. Multiplicar'
              + '\n5. Potência'
              + '\n6. Raiz'
              + '\n7. Tabuada'
              + '\n8. Imprimir 1 ao 10'
              + '\n9. Imprimir pares 1 ao 20'
              + '\n10. Somar do 1 ao 100'
              + '\n11. Tabuada do 5'
              + '\n12. Par ou Impar'
              + '\n13. Positivo, Negativo ou Zero'
              + '\n14. Imprimir 1 ao número'
              + '\n15. Somar do 1 até o número'
              + '\n16. Imprimir ímpares 1 ao 20'
              + '\n17. Primo'
              + '\n18. Fatorial'
              + '\n19. Fibonacci'
              + '\n20. Somar dígitos'
              + '\n21. Pares e ímpares'
              + '\n22. Imprimir primos'
              + '\n23. Somar todos'
              + '\n24. Sequencia de Collatz'
              + '\n25. Número perfeito'
              + '\n\n\n ------ 2ª Lista ------ \n\n'
              + '\n26. Troca'
              + '\n27. Antecessor'
              + '\n28. Àrea do Retangulo'
              + '\n29. Anos em Dias'
              + '\n30. Votos'
              + '\n31. Reajuste de salário'
              + '\n32. Preço total do carro'
              + '\n33. Média do aluno'
              + '\n34. Preço das maçãs'
              + '\n35. Ordem crescente'
              + '\n36. Salário após comissão'
              + '\n37. Saldo atual'
              + '\n38. Tabuada do 1 ao 10'
              + '\n39. Imprimir valores'
              + '\n40. Números negativos'
              + '\n41. Somar menores que 40'
              + '\n42. Média do 15 ao 100'
              + '\n43. Quantidade'
              + '\n44. Média da turma'
              + '\n45. Prefeitura'



              )


    def coletar(self):

        self.num1 = int(input("Informe o primeiro número: "))
        self.num2 = int(input("Informe o segundo número: "))


    def executar(self):
        while self.opcao != 0:
            self.mostrarmenu()
            self.opcao = int(input('Escolha uma das opções do MENU: '))

            if self.opcao == 0:
                print('Obrigado!')
            elif self.opcao == 1:
                self.coletar() #Chamando o input
                print(f'\nA soma dos números é: {self.opera.somar(self.num1, self.num2)}')

            elif self.opcao == 2:      #ELIF é o mesmo que else if
                self.coletar()
                print(f'\nA subtração dos números é: {self.opera.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'\nA divisão dos números é: {self.opera.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'\nA multiplicação dos números é: {self.opera.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'\nA potência dos números é: {self.opera.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'\nA raiz do {self.num1} é: {self.opera.raiz(self.num1)}')
                print(f'\nA raiz do {self.num2} é: {self.opera.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'\nA tabuada do {self.num1} é: {self.opera.tabuada(self.num1)}')
                print(f'\nA tabuada do {self.num2} é: {self.opera.tabuada(self.num2)}')

            elif self.opcao == 8:

                print(f'\n {self.opera.imprimir()}')

            elif self.opcao == 9:

                print(f'\n {self.opera.pares()}')

            elif self.opcao == 10:

                print(f'\nA soma do 1 ao 100 é {self.opera.soma()}')

            elif self.opcao == 11:

                print(f'\nTabuada do 5 \n{self.opera.multiplos()}')

            elif self.opcao == 12:
                self.coletar()
                print(f'\nPar ou Impar \n{self.opera.parouimpar(self.num1)}')
                print(f'\nPar ou Impar \n{self.opera.parouimpar(self.num2)}')

            elif self.opcao == 13:
                self.coletar()
                print(f' \n{self.opera.numero(self.num1)}')
                print(f' \n{self.opera.numero(self.num2)}')

            elif self.opcao == 14:
                self.coletar()
                print(f'\n {self.opera.ate(self.num1)}')
                print(f'\n {self.opera.ate(self.num2)}')

            elif self.opcao == 15:
                self.coletar()
                print(f'\nA soma do 1 ao {self.num1} é \n{self.opera.somatodos(self.num1)}')
                print(f'\nA soma do 1 ao {self.num2} é \n{self.opera.somatodos(self.num2)}')

            elif self.opcao == 16:

                print(f'\n {self.opera.impares()}')

            elif self.opcao == 17:
                self.coletar()
                print(f' \n{self.opera.primo(self.num1)}')
                print(f' \n{self.opera.primo(self.num2)}')

            elif self.opcao == 18:
                self.coletar()
                print(f'\n O fatorial de {self.num1} é {self.opera.fatorial(self.num1)}')
                print(f' \n O fatorial de {self.num2} é {self.opera.fatorial(self.num2)}')

            elif self.opcao == 19:
                self.coletar()
                print(f'\n {self.opera.fibonacci(self.num1)}')
                print(f'\n {self.opera.fibonacci(self.num2)}')

            elif self.opcao == 20:
                num1 = int(input('Informe um número: '))
                print(f'\nA soma dos dígitos de {self.num1} é: {self.opera.digitos(num1)}')

            elif self.opcao == 21:
                self.coletar()
                print(f' \n{self.opera.imprimirtodos(self.num1)}')
                print(f' \n{self.opera.imprimirtodos(self.num2)}')

            elif self.opcao == 22:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.imprimirprimos(num1)}')

            elif self.opcao == 23:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.somatodos2(num1)}')

            elif self.opcao == 24:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.collatz(num1)}')

            elif self.opcao == 25:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.perfeito(num1)}')

            elif self.opcao == 26:
                print(f' \n{self.opera.troca()}')

            elif self.opcao == 27:
                num1 = int(input('Informe um número: '))
                print(f' \n{self.opera.antecessor(num1)}')


            elif self.opcao == 28:
                num1 = int(input('Informe a base: '))
                num2 = int(input('Informe a altura: '))
                print(f'\nA área do retangulo é:  {self.opera.areaRe(num1,num2)}')

            elif self.opcao == 29:
                num1 = int(input('Informe o ano Atual: '))
                num2 = int(input('Informe o ano de nascimento: '))
                num3 = int(input('Informe o mês: '))
                num4 = int(input('Informe o dia: '))
                print(f'\nA idade em dias é:  {self.opera.anosDia(num1, num2,num3,num4)}')

            elif self.opcao == 30:
                num1 = int(input('Informe o total de votos: '))
                num2 = int(input('Informe os votos brancos: '))
                num3 = int(input('Informe os votos nulos: '))
                num4 = int(input('Informe os votos validos: '))
                print(f' \n{self.opera.votos(num1, num2,num3,num4)}')

            elif self.opcao == 31:
                num1 = int(input('Informe o salário atual: '))
                num2 = int(input('Informe o percentual de ajuste: '))
                print(f'\nO novo salário é:  {self.opera.salario(num1, num2)}')

            elif self.opcao == 32:
                num1 = int(input('Informe o custo de fábrica do carro: '))
                print(f'\nO valor total do carro é:  {self.opera.carro(num1)}')

            elif self.opcao == 33:
                num1 = int(input('Informe a primeira nota: '))
                num2 = int(input('Informe a segunda nota: '))
                num3 = int(input('Informe a terceira nota: '))
                print(f'\n A média desse aluno é: {self.opera.media(num1, num2, num3)}')

            elif self.opcao == 34:
                num1 = int(input('Informe a quantidade de maçãs: '))
                print(f'\nO valor total é:  {self.opera.maca(num1)}')

            elif self.opcao == 35:
                vetor = []
                for i in range(1,11,1):
                    vetor.append(input(f'Informe o {i}º valor: '))
                print(f'\nA ordem crescente dos valores é:  {self.opera.crescente(vetor)}')

            elif self.opcao == 36:
                num1 = int(input('Informe o salário fixo: '))
                num2 = int(input('Informe o valor das vendas: '))
                print(f'\nO salário total é:  {self.opera.vendas(num1,num2)}')

            elif self.opcao == 37:
                num1 = int(input('Informe o saldo: '))
                num2 = int(input('Informe o débito: '))
                num3 = int(input('Informe o crédito: '))
                print(f'\nSobre o saldo atual do cliente da conta 12345: \n  {self.opera.saldo(num1,num2,num3)}')

            elif self.opcao == 38:
                num = int(input('Informe um número de 1 a 10: '))
                print(f'\nA tabuada é:  {self.opera.tabua(num)}')

            elif self.opcao == 39:
                num = int(input('Informe um número inteiro: '))
                print(f'\n {self.opera.imprima(num)}')

            elif self.opcao == 40:
                vetor = []
                for i in range(1, 11, 1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'\nTem   {self.opera.negativos(vetor)} valores negativos')

            elif self.opcao == 41:
                vetor = []
                for i in range(1, 11, 1):
                    vetor.append(int(input(f'Informe o {i}º valor: ')))
                print(f'\nA soma de todos os números abaixo de quarenta é:  {self.opera.somaQuarenta(vetor)}')

            elif self.opcao == 42:
                print(f'\nA média aritmética do 15 ao 100 é:  {self.opera.mediaArit()}')

            elif self.opcao == 43:
                num = int(input('Informe uma quantidade: '))
                vetor = []
                for i in range(0, num, 1):
                    vetor.append(int(input(f'Informe o {i+1}º valor: ')))
                print(f'\n {self.opera.quantidade(vetor)}')

            elif self.opcao == 44:
                vetor = []
                for i in range(0, 20, 1):
                    vetor.append(int(input(f'Informe o {i + 1}º valor: ')))
                print(f'\n {self.opera.mediaAlunos(vetor)}')

            elif self.opcao == 45:
                num = int(input('Informe o total de pessoas: '))
                salario = []
                filho = []
                for i in range(0, num, 1):
                    salario.append(int(input(f'Informe o {i + 1}º salário: ')))
                for i in range(0, num, 1):
                    filho.append(int(input(f'Informe a {i + 1}º quantidade de filhos: ')))
                print(f'\n {self.opera.prefeitura(salario,filho)}')






            else:
                return "Número inválido"









