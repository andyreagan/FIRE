from definitions import *


def find_college_savings(bond, bond_sd,
                         stock, stock_sd,
                         bond_stock_corr,
                         ages: list) -> list:
    '''
    Find the yearly savings until age 120.
    '''
    beginning_ratio = [80, 20]
    end_ratio = [20, 80]
    cost = college['private']


def make_withdrawals(expenses, balances):
    '''
    Make withdrawals needed to support expenses.
    Do the required minimum on 401(k) accounts first.
    Pull from accounts that don't have a penalty first too.
    '''


def make_contributions(savings, balances):
    '''
    The simplist thing to do: distribute 19.5 to 401k and the rest to taxable.
    '''


def update_growth(rates):
    '''
    Compute the growth in each account.
    '''


def draw_rate(bond, bond_sd,
              stock, stock_sd,
              bond_stock_corr):
    '''
    Draw a rate.
    '''


def simulate(bond, bond_sd,
             stock, stock_sd,
             bond_stock_corr,
             income,
             retirement_age: int,
             beginning_balances: dict,
             contrib_balance: dict) -> list:
    '''
    Generate the probability of running out of money at any age.
    '''
    year = 0
    balances = [beginning_balances]
    while retirement_age + year < 120:
        year += 1
        # draw a growth rate
        rates = draw_rate(bond, bond_sd, stock, stock_sd, corr)
        # then update
        new_balances = update_growth(balances, rates)
        new_balances += make_contributions(income, contrib_balance)
        new_balances += make_withdrawals(year, expenses)
        balances.append(new_balances)
    return balances


def main():
    projection = simulate(.2, .1, .4, .1, .7, 100000, 45, {'401k': 20000, '401k_roth': 0, 'IRA': 0, 'IRA_roth': 0, 'taxable': 10000}, {'401k': 'max', 'taxable': 'balance'})
    success_rate = cumsum(project[income > 0])
    print(projection)
