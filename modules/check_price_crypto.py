import requests
from aiogram import types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import CommandObject
from aiogram import Router  

COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
router = Router()

# Пример использования: /crypto bitcoin
@router.message(Command("crypto"))
async def crypto_price(message: Message, command: CommandObject):
    if command.args:
        crypto_symbol = command.args.upper()
        crypto_price = get_crypto_price(crypto_symbol)
        if crypto_price:
            await message.reply(f"Текущий курс {crypto_symbol.upper()}: {crypto_price} USD")
        else:
            await message.reply(f"Не удалось получить информацию о курсе {crypto_symbol.upper()}")
    else:
        await message.reply("Пожалуйста, укажите криптовалюту после команды /crypto")


def get_crypto_price(crypto_symbol):
    params = {
        'ids': crypto_symbol.lower(),
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
    "BTC": "Bitcoin",
    "ETH": "Ethereum",
    "USDT": "Tether",
    "BNB": "BNB",
    "XRP": "XRP",
    "SOL": "Solana",
    "USDC": "USDC",
    "STETH": "Lido Staked Ether",
    "ADA": "Cardano",
    "DOGE": "Dogecoin",
    "TRX": "TRON",
    "TON": "Toncoin",
    "LINK": "Chainlink",
    "AVAX": "Avalanche",
    "MATIC": "Polygon",
    "DOT": "Polkadot",
    "WBTC": "Wrapped Bitcoin",
    "DAI": "Dai",
    "LTC": "Litecoin",
    "SHIB": "Shiba Inu",
    "UNI": "Uniswap",
    "BCH": "Bitcoin Cash",
    "LEO": "LEO Token",
    "OKB": "OKB",
    "XLM": "Stellar",
    "TUSD": "TrueUSD",
    "XMR": "Monero",
    "KAS": "Kaspa",
    "ATOM": "Cosmos Hub",
    "ETC": "Ethereum Classic",
    "CRO": "Cronos",
    "FIL": "Filecoin",
    "ICP": "Internet Computer",
    "LDO": "Lido DAO",
    "HBAR": "Hedera",
    "APT": "Aptos",
    "RUNE": "THORChain",
    "NEAR": "NEAR Protocol",
    "BUSD": "BUSD",
    "MNT": "Mantle",
    "IMX": "Immutable",
    "VET": "VeChain",
    "OP": "Optimism",
    "TAO": "Bittensor TAO",
    "QNT": "Quant",
    "AAVE": "Aave",
    "INJ": "Injective",
    "MKR": "Maker",
    "GRT": "The Graph",
    "ARB": "Arbitrum",
    "RETH": "Rocket Pool ETH",
    "RNDR": "Render",
    "EGLD": "MultiversX EGLD",
    "SNX": "Synthetix Network",
    "STX": "Stacks",
    "ALGO": "Algorand",
    "FLOW": "Flow",
    "THETA": "Theta Network",
    "BSV": "Bitcoin SV",
    "TIA": "Celestia",
    "FTM": "Fantom",
    "AXS": "Axie Infinity",
    "SAND": "The Sandbox",
    "FDUSD": "First Digital USD",
    "MANA": "Decentraland",
    "KCS": "KuCoin",
    "WBT": "WhiteBIT Coin",
    "EOS": "EOS",
    "NEO": "NEO",
    "BGB": "Bitget Token",
    "XTZ": "Tezos",
    "KAVA": "Kava",
    "GALA": "GALA",
    "USDD": "USDD",
    "MINA": "Mina Protocol",
    "IOTA": "IOTA",
    "XDC": "XDC Network",
    "ILV": "Illuvium",
    "LUNC": "Terra Luna Classic",
    "FRAX": "Frax",
    "WEMIX": "WEMIX",
    "KLAY": "Klaytn",
    "PYTH": "Pyth Network",
    "FRXETH": "Frax Ether",
    "TKX": "Tokenize Xchange",
    "CHEEL": "Cheelee",
    "GT": "Gate",
    "SUI": "Sui",
    "APE": "ApeCoin",
    "BLUR": "Blur",
    "XEC": "eCash",
    "ETHDYDX": "dYdX ETHDYDX",
    "FET": "Fetch.ai",
    "RPL": "Rocket Pool RPL",
    "FXS": "Frax Share",
    "CFX": "Conflux",
    "AR": "Arweave",
    "CAKE": "PancakeSwap",
    "GAS": "Gas",
    "XRD": "Radix",
}

