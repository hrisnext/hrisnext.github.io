from .models import Paycal
from .rates import qcrates

def get_earning_pp(hours, hourlyRate):
  if hours and hourlyRate:
    earning_pp = hours*hourlyRate
  return earning_pp
    
def nomarlizeNumber(value, interval):
  _value = +value
  _min = int(interval[0])
  _max = int(interval[1])
  if _value < _min:
      return _min
  elif _value >= _min and _value <= _max:
      return _value
  else:
      return _max
def findIdx(array, val):
  if val <= min(array):
      return 0
  if val > max(array):
      return len(array)
  idx, i, j = 0, 0, len(array)

  for i in range(j):
      if array[i] >= val:
          idx = i
          return idx
def getSrcDeduc(earning_pp):
  if earning_pp:
    wcb_er = round(float(earning_pp*float(qcrates.wcb_er_rate)),2)
    ei_er = round(float(earning_pp*float(qcrates.ei_er_rate)),2)
    cpp_er = round(float(earning_pp*float(qcrates.cpp_er_rate)),2)
    ei_ee = round(float(earning_pp*float(qcrates.ei_ee_rate)),2)
    cpp_ee = round(float(earning_pp*float(qcrates.cpp_ee_rate)),2)
    qpip_ee = round(float(earning_pp*float(qcrates.qpip_ee_rate)),2)
    cnt_er = round(float(earning_pp*float(qcrates.cnt_er_rate)),2)
    hsf_er = round(float(earning_pp*float(qcrates.hsf_er_rate)),2)
    qpip_er = round(float(earning_pp*float(qcrates.qpip_er_rate)),2)
    srcDeduc = ei_ee + cpp_ee + qpip_ee
  return wcb_er, ei_er, cpp_er, ei_ee, cpp_ee, qpip_ee, cnt_er, hsf_er, qpip_er

def getIncomeTaxPr():
  index = findIdx(rates.fdrates.fRange, pp_earning)
  taxRate = rates.fdrates.fRate[index]
  quickDeduction = rates.fdrates.fQuickDeduction
  tax = (pp_earning*26*taxRate - quickDeduction)/26
  afterTax = pp_earning - tax - srcDeduc
  
'''
export function getIncomeTax(
  income,
  insurance,
  month = 12,
  deduction = 0,
  threshold = 5000
) {
  const totalIncome = +(+income * month).toFixed(2);
  const totalDeduction = +(
    (+insurance + deduction + threshold) *
    month
  ).toFixed(2);
  const totalInsurance = +(+insurance * month).toFixed(2);
  const taxableIncome = totalIncome - totalDeduction;
  const aRange = [0, 36000, 144000, 300000, 420000, 660000, 960000];
  const aTaxRate = [0, 3, 10, 20, 25, 30, 35, 45];
  const aQuickDeduction = [0, 0, 2520, 16920, 31920, 52920, 85920, 181920];
  const index = find(aRange, taxableIncome);
  const taxRate = aTaxRate[index];
  const quickDeduction = aQuickDeduction[index];
  const tax = +((taxableIncome * taxRate) / 100 - quickDeduction).toFixed(2);
  const afterTax = +((+income - +insurance) * month - tax).toFixed(2);

  return {
    taxRate,
    quickDeduction,
    tax,
    afterTax,
    income: totalIncome,
    totalDeduction,
    totalInsurance
  };
}

export function getInsurance(
  IBase,
  HACBase,
  index,
  checkProvident = true,
  HACRate
) {
  const {
    MIBases,
    EIBases,
    UIBases,
    EIRates,
    MIRates,
    UIRates,
    addMI
  } = INSURANCE[index];
  const MI = nomarlizeNumber(IBase, MIBases) * MIRates[0] + addMI;
  const EI = nomarlizeNumber(IBase, EIBases) * EIRates[0];
  const UI = nomarlizeNumber(IBase, UIBases) * UIRates[0];
  return +(MI + EI + UI + HACBase * HACRate * Number(checkProvident)).toFixed(
    2
  );
}

'''