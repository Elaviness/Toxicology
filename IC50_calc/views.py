import rdkit.Chem
import numpy as np
from django.shortcuts import render
from .models import Chemistry, SearchList
from rdkit.Chem import MolFromSmiles, Draw
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit import Chem, DataStructs
from rdkit.Chem import Descriptors

from django.http import HttpResponse
from .gb_model import gbm


# Create your views here.
def main(request):
    return render(request, 'IC50_calc/main.html')


def base(request):
    table = Chemistry.objects.all()
    for row in table:
        if not row.image:
            row.image = generate_image(row.id, row.smile)
            row.save(update_fields=['image'])

    return render(request, 'IC50_calc/base.html', context={'table': table})


def about(request):
    return render(request, 'IC50_calc/about.html')


def calc(request):
    smile = request.GET.get('search')
    if smile:
        result = get_calc(smile)
        if not result:
            error = True
        else:
            error = False
        return render(request, 'IC50_calc/calc.html', context={'result': result, 'error': error})
    else:
        return render(request, 'IC50_calc/calc.html', context={'result': None, "error": False})


def get_calc(smile):
    if Chem.MolFromSmiles(smile):
        try:
            fm = Chemistry.objects.get(smile=smile)
        except:
            fm = None
        check_fp = find_fingerprint(smile)
        if fm:
            result = SearchList.objects.create(smile=fm.smile, flag=False, image=fm.image, ic50=fm.ic50)
            return result
        elif check_fp:
            fm = Chemistry.objects.get(smile=check_fp)
            result = SearchList.objects.create(smile=fm.smile, flag=False, image=fm.image, ic50=fm.ic50)
            return result
        else:
            info = get_one_chem_info(smile)
            ic50 = round(gbm.predict(info)[0], 3)
            obj = SearchList.objects.create(smile=smile, flag=True, ic50=ic50)
            obj.image = generate_new_image(obj.id, obj.smile)
            obj.save()
            return obj
    else:
        return None



def generate_image(id, smile):
    mol = MolFromSmiles(smile)
    img = Draw.MolToFile(mol, f'IC50_calc/img/{id}.png')
    return f'{id}.png'

def find_fingerprint(smile):
    m = rdkit.Chem.MolFromSmiles(smile)
    f = FingerprintMols.FingerprintMol(m)
    full = Chemistry.objects.all()
    for row in full:
        mol = rdkit.Chem.MolFromSmiles(row.smile)
        new_f = FingerprintMols.FingerprintMol(mol)
        if DataStructs.FingerprintSimilarity(f, new_f) == 1.0:
            return row.smile
        else:
            return False

def get_one_chem_info(smile):
    m = Chem.MolFromSmiles(smile)
    return np.array([Descriptors.MolLogP(m),
                    Descriptors.TPSA(m),
                    Descriptors.NHOHCount(m),
                    Descriptors.NOCount(m),
                    Descriptors.NumHAcceptors(m),
                    Descriptors.NumHDonors(m),
                    Descriptors.NumRotatableBonds(m),
                    Chem.rdMolDescriptors.CalcNumAmideBonds(m),
                    Descriptors.NumHeteroatoms(m),
                    Descriptors.NumValenceElectrons(m),
                    Chem.rdMolDescriptors.CalcNumSpiroAtoms(m),
                    Descriptors.FractionCSP3(m),
                    Descriptors.FpDensityMorgan1(m),
                    Descriptors.ExactMolWt(m),
                    Descriptors.Chi0(m),
                    Descriptors.Chi1(m),
                    Descriptors.Ipc(m),
                    Descriptors.BertzCT(m),
                    Descriptors.LabuteASA(m)]).reshape(-1, 19)

def generate_new_image(id, smile):
    mol = MolFromSmiles(smile)
    img = Draw.MolToFile(mol, f'IC50_calc/img/search/{id}.png')
    return f'search/{id}.png'



