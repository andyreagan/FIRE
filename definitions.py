college = {"public": 16784, "private": 36763}

fourzeroonek = {"max_contrib": 19500, "max_contrib_over_50": 26000, "growth_tax": "deferred", "min_draw_age": 59.5,
                "early_withdrawal_penalty": 0.10, "max_total": 56000, "rmd_age": 70.5, "contrib_tax": "pre"}

# same rules, except tax differences
fourzeroonek_roth = fourzeroonek
fourzeroonek_roth["growth_tax"] = "free"
fourzeroonek_roth["contrib_tax"] = "post"

ira = {"growth_tax": "deferred", "contrib_tax": "pre"}

ira_roth = {"max_contrib": 6500, "growth_tax": "free", "contrib_tax": "post"}

# this is taxed on capital gains when trades are made
# interest and dividends are also taxed
taxable = {"growth_tax": "taxed", "contrib_tax": "post"}

irs_rmd_lookup = {56: 28.7,
                  57: 27.9,
                  58: 27.0,
                  59: 26.1,
                  60: 25.2,
                  61: 24.4,
                  62: 23.5,
                  63: 22.7,
                  64: 21.8,
                  65: 21.0,
                  66: 20.2,
                  67: 19.4,
                  68: 18.6,
                  69: 17.8,
                  70: 17.0,
                  71: 16.3,
                  72: 15.5,
                  73: 14.8,
                  74: 14.1,
                  75: 13.4,
                  76: 12.7,
                  77: 12.1,
                  78: 11.4,
                  79: 10.8,
                  80: 10.2,
                  81: 9.7,
                  82: 9.1,
                  83: 8.6,
                  84: 8.1,
                  85: 7.6,
                  86: 7.1,
                  87: 6.7,
                  88: 6.3,
                  89: 5.9,
                  90: 5.5,
                  91: 5.2,
                  92: 4.9,
                  93: 4.6,
                  94: 4.3,
                  95: 4.1,
                  96: 3.8,
                  97: 3.6,
                  98: 3.4,
                  99: 3.1,
                  100: 2.9,
                  101: 2.7,
                  102: 2.5,
                  103: 2.3,
                  104: 2.1,
                  105: 1.9,
                  106: 1.7,
                  107: 1.5,
                  108: 1.4,
                  109: 1.2,
                  110: 1.1,
                  111: 1.0}


def rmd(age: int, balance: float, irs_lookup: dict) -> float:
    return (balance / irs_lookup[age])
