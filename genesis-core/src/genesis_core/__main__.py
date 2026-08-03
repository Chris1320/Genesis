import argparse
import sys

import uvicorn

from genesis_core.main import app


def main(host: str, port: int) -> None:
    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Your journal, only yours.")
    _ = parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Host to run the server on (default: 127.0.0.1)",
    )
    _ = parser.add_argument(
        "--port",
        type=int,
        default=8081,
        help="Port to run the server on (default: 8081)",
    )

    args = parser.parse_args()

    host: str = args.host  # pyright: ignore[reportAny]
    port: int = args.port  # pyright: ignore[reportAny]
    sys.exit(main(host, port))
