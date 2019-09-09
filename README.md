# conjugacaoScraper #


[![GitHub license](https://img.shields.io/github/license/bartier/conjugacaoScraper)](https://github.com/bartier/conjugacaoScraper/blob/master/LICENSE)

`conjugacaoScraper` é um projeto com fins de estudos que obtém informações do [Conjugacoes](http://conjugacao.com.br/). 
Utiliza o [Scrapy](http://scrapy.org/) como base. 

# Instalação #
Como requisito é necessário ter [Pipenv](https://pipenv-es.readthedocs.io/es/stable/). 

Para instalá-lo utilize o pip:
```
$ pip install pipenv
```

Passos necessários para obter o projeto funcional:

    $ git clone https://github.com/bartier/conjugacaoScraper.git
    $ cd conjugacaoScraper/
    $ pipenv install
    $ pipenv shell
    $ scrapy list
    $ Se a saída do comando acima for 'verbs' você está com o projeto pronto.
	
	
O projeto é executado dentro de um environment virtual, ou seja caso você precise acessá-lo novamente utilize:
```
$ pipenv shell
```

# Spiders #

## VerbsSpider

VerbsSpider é um spider que obtém os verbos da listagem que inicia [nessa URL](https://www.conjugacao.com.br/verbos-populares/1/).
A listagem obtém cerca de 5000 verbos.

Para utilizá-lo execute o comando abaixo:
```
$ scrapy crawl verbs -o verbs.json
```

A listagem dos verbos será salva no arquivo *verbs.json* no diretório raiz do projeto.

