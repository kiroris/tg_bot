import requests
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import CommandObject
from aiogram import Router  

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
router = Router()

@router.message(Command("crypto"))
async def crypto_price(message: Message, command: CommandObject):
    if command.args:
        crypto_abbr = command.args.upper()
        crypto_symbol = crypto_dict[crypto_abbr] 
        crypto_price = get_crypto_price(crypto_symbol)

        if crypto_price:
            await message.reply(f"Текущий курс {crypto_symbol.upper()}: {crypto_price} USD")
        else:
            await message.reply(f"Не удалось получить информацию о курсе {crypto_symbol.upper()}")
    else:
        await message.reply("Пожалуйста, укажите криптовалюту после команды /crypto")


def get_crypto_price(crypto_symbol):
    params = {
        'ids': crypto_symbol,
        'vs_currencies': 'usd',
    }

    try:
        response = requests.get(COINGECKO_API_URL, params=params)
        data = response.json()

        if response.status_code == 200 and crypto_symbol.lower() in data:
            return data[crypto_symbol.lower()]['usd']
        else:
            print(f"Ошибка при получении данных: {response.status_code}, {response.text}")
            return None

    except Exception as e:
        print(f"Произошла ошибка: {e}")


crypto_dict = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDT": "tether",
    "BNB": "bnb",
    "XRP": "xrp",
    "SOL": "solana",
    "USDC": "usdc",
    "STETH": "lido staked ether",
    "ADA": "cardano",
    "DOGE": "dogecoin",
    "TRX": "tron",
    "TON": "toncoin",
    "LINK": "chainlink",
    "AVAX": "avalanche",
    "MATIC": "polygon",
    "DOT": "polkadot",
    "WBTC": "wrapped bitcoin",
    "DAI": "dai",
    "LTC": "litecoin",
    "SHIB": "shiba inu",
    "UNI": "uniswap",
    "BCH": "bitcoin cash",
    "LEO": "leo token",
    "OKB": "okb",
    "XLM": "stellar",
    "TUSD": "trueusd",
    "XMR": "monero",
    "KAS": "kaspa",
    "ATOM": "cosmos hub",
    "ETC": "ethereum classic",
    "CRO": "cronos",
    "FIL": "filecoin",
    "ICP": "internet computer",
    "LDO": "lido dao",
    "HBAR": "hedera",
    "APT": "aptos",
    "RUNE": "thorchain",
    "NEAR": "near protocol",
    "BUSD": "busd",
    "MNT": "mantle",
    "IMX": "immutable",
    "VET": "vechain",
    "OP": "optimism",
    "TAO": "bittensor tao",
    "QNT": "quant",
    "AAVE": "aave",
    "INJ": "injective",
    "MKR": "maker",
    "GRT": "the graph",
    "ARB": "arbitrum",
    "RETH": "rocket pool eth",
    "RNDR": "render",
    "EGLD": "multiversx egld",
    "SNX": "synthetix network",
    "STX": "stacks",
    "ALGO": "algorand",
    "FLOW": "flow",
    "THETA": "theta network",
    "BSV": "bitcoin sv",
    "TIA": "celestia",
    "FTM": "fantom",
    "AXS": "axie infinity",
    "SAND": "the sandbox",
    "FDUSD": "first digital usd",
    "MANA": "decentraland",
    "KCS": "kucoin",
    "WBT": "whitebit coin",
    "EOS": "eos",
    "NEO": "neo",
    "BGB": "bitget token",
    "XTZ": "tezos",
    "KAVA": "kava",
    "GALA": "gala",
    "USDD": "usdd",
    "MINA": "mina protocol",
    "IOTA": "iota",
    "XDC": "xdc network",
    "ILV": "illuvium",
    "LUNC": "terra luna classic",
    "FRAX": "frax",
    "WEMIX": "wemix",
    "KLAY": "klaytn",
    "PYTH": "pyth network",
    "FRXETH": "frax ether",
    "TKX": "tokenize xchange",
    "CHEEL": "cheelee",
    "GT": "gate",
    "SUI": "sui",
    "APE": "apecoin",
    "BLUR": "blur",
    "XEC": "ecash",
    "ETHDYDX": "dydx ethdydx",
    "FET": "fetch.ai",
    "RPL": "rocket pool rpl",
    "FXS": "frax share",
    "CFX": "conflux",
    "AR": "arweave",
    "CAKE": "pancakeswap",
    "GAS": "gas",
    "XRD": "radix",
}
