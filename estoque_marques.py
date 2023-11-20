import typing
import datetime

Produto = typing.NewType("Produto", str)
Pessoa = typing.NewType("Pessoa", str)
Venda = typing.NewType("Venda", str) 
Compra = typing.NewType("Compra", str)

class Pessoa():
    def __init__(self, nome, telefone, endereco, cpf, nascimento):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cpf = cpf
        self.nascimento = nascimento

class Funcionario(Pessoa):
    def __init__(self, salario):
        self.salario = salario

class Vendedor(Funcionario):
    def __init__(self):
        return None

    def verificarEstoque(produto:Produto):
        estoque_produto = Produto.estoque
        return estoque_produto
    
    def iniciarVenda():
        return Venda
    
    def adicionaraoCarrinho(venda:Venda, produto:Produto, quantidade):
        return None
    
    def fecharVenda(venda:Venda):
        return None

    

class Gerente(Funcionario):
    def __init__(self):
        return None

    def gerarRelatorio(produto:Produto):
        return RelatorioProduto
    
    def gerarRelatorios():
        return RelatorioProduto
    
    def abrirCompra():
        return Compra
    
    def fecharCompra(compra:Compra):
        return None

class Transacao():
    def __init__(self, itens):
        itens = []
        self.itens = itens
        self.data = datetime.now()
    
    def getvalorTotal():
        return float

class ItemTransacao(Transacao):
    def __init__(self, quantidade, produto:Produto):
        self.produto = produto
        self.quantidade = quantidade

    def getValorItem():
        return float

class RelatorioProduto():
    def __init__(self, quantidadeComprada, quantidadeVendida, estoqueRestante):
        self.quantidadeComprada = quantidadeComprada
        self.quantidadeVendida = quantidadeVendida
        self.quantidadeRestante = estoqueRestante



class Produto(ItemTransacao):
    def __init__(self, id, nome, preco, custo, imposto, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.custo = custo
        self.imposto = imposto
        self.estoque = estoque


class Venda(Transacao):
    def __init__(self, Cliente, frete):
        self.frete = frete 
        self.cliente = Cliente
    
    def calcularFrete(endereco:str):
        return float
    
    def adicionaraoCarrinho(produto:Produto):
        return None

class Compra(Transacao):
    def __init__(self, fornecedor):
        self.fornecedor = fornecedor

class Cliente(Pessoa):
    def __init__():
        return None
    
class Fornecedor(Pessoa):
    def __init__():
        return None