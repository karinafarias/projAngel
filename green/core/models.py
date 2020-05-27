from django.db import models

# Create your models here.
class Polo (models.Model):
    nomePolo = models.CharField(max_length=100)
    qtdEstoque = models.IntegerField(default=0)

class Meta:
    db_table = 'polo'

def __str__(self):
    return self.nomePolo


class Terminal (models.Model):
    serialTerminal = models.IntegerField()
    status = models.BooleanField(default=True)
    idPoloT = models.ForeignKey(Polo, on_delete=models.PROTECT)

class Meta:
    db_table = 'terminal'

    def __str__(self):
        return self.serialTerminal


class Historico(models.Model):
    dataHistorico = models.DateTimeField(auto_now=True)
    idPoloH = models.ForeignKey(Polo, on_delete=models.PROTECT)
    idTerminalH= models.ForeignKey(Terminal, on_delete=models.PROTECT)

class Meta:
    db_table = 'historico'

    def getDataHistorico(self):
        return self.dataHistorico.strftime('%d/%m/%Y %H:%M')