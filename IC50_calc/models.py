from django.db import models


class Chemistry(models.Model):
    smile = models.CharField(max_length=50)
    image = models.ImageField(default=None, null=True)
    mol_log = models.FloatField()
    tpsa = models.FloatField()
    nhoh_count = models.IntegerField()
    no_count = models.IntegerField()
    num_ha_acceptors = models.IntegerField()
    num_h_donors = models.IntegerField()
    num_rotatable_bonds = models.IntegerField()
    calc_num_amide_bonds = models.IntegerField()
    num_heteroatoms = models.IntegerField()
    num_valence_electrons = models.IntegerField()
    num_spiro_atoms = models.IntegerField()
    fraction_csp3 = models.FloatField()
    fp_density_morgan1 = models.FloatField()
    exact_mol_wt = models.FloatField()
    chi0 = models.FloatField()
    ch1 = models.FloatField()
    ipc = models.FloatField()
    bertz_ct = models.FloatField()
    labute_asa = models.FloatField()
    ic50 = models.FloatField()

    def __str__(self):
        return f'{self.smile}'

class SearchList(models.Model):
    smile = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    flag = models.BooleanField()
    ic50 = models.FloatField()

    def __str__(self):
        return f'{self.smile}'
