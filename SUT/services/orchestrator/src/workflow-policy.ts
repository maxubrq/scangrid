// Workflow Policy: hàm thuần quyết định stage tiếp theo của một item.
// Không I/O, không Date.now(), không Math.random(): oracle 5 chạy lại hàm này offline trên lịch sử.
import type { EngineRole, ItemId, OutcomeStatus, ScanPolicy } from "@scangrid/domain";

/** Ảnh chụp trạng thái của MỘT item (mô hình task, mục 8.7), không phải cả cây. */
export interface ItemSnapshot {
  readonly itemId: ItemId;
  readonly fileType: string | undefined;
  readonly depth: number;
  /** Outcome cuối cùng theo engine, cho lần thử được chọn. */
  readonly outcomes: Readonly<Record<string, OutcomeStatus>>;
  /** Engine đã được lên lịch cho item này (mọi lần thử). */
  readonly scheduled: ReadonlyArray<{ engine: string; attempt: number }>;
}

export interface PlannedTask {
  readonly engine: string;
  readonly role: EngineRole;
  readonly attempt: number;
}

export type StageDecision =
  | { readonly kind: "dispatch"; readonly tasks: ReadonlyArray<PlannedTask> }
  | { readonly kind: "item_done" };

export function planNextStage(_policy: ScanPolicy, _item: ItemSnapshot): StageDecision {
  // TODO(Block 4, bước 2): 3 workflow — chỉ AV; AV cùng CDR rồi DLP; AV, nghi ngờ thì sandbox.
  throw new Error("not implemented: planNextStage");
}
