import pathlib
from craftax.environment_base.util import load_compressed_pickle

def test_import():
    TEXTURE_CACHE_FILE = pathlib.Path(__file__).parent.resolve() / "craftax_classic" / "assets" / "texture_cache_classic.pbz2"

    TEXTURE_CACHE_FILE.unlink(missing_ok=True)

    import craftax.craftax_classic.constants  # noqa: F401
    assert TEXTURE_CACHE_FILE.exists(), "import should have created texture cache file"

    _textures = load_compressed_pickle(TEXTURE_CACHE_FILE)
