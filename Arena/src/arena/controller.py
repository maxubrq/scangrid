"""Service điều khiển battle (Block 3, bước 4): start, stop, trạng thái."""

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Arena controller")


@app.post("/battles/{battle_id}/start")
def start(battle_id: str, seed: int) -> None:
    raise HTTPException(501, f"TODO(Block 3): start {battle_id} seed={seed}")


@app.post("/battles/{battle_id}/stop")
def stop(battle_id: str) -> None:
    raise HTTPException(501, f"TODO(Block 3): stop {battle_id}")


@app.get("/battles/{battle_id}")
def status(battle_id: str) -> None:
    # A4: đang ở phase nào, lỗi nào đang bật, còn bao lâu.
    raise HTTPException(501, f"TODO(Block 3): status {battle_id}")
