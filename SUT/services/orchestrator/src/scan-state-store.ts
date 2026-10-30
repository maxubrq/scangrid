// Scan State Store: một interface, hai chiến lược (Block 4, bước 7).
//   v1 "by-engine": chia trạng thái theo loại engine như hệ thống cũ (O(n) mỗi outcome).
//   v2 "by-task":   hash meta + hash mỗi item + sorted set deadline, cùng hash tag {scanId}.
// Arena chạy B8 và B16 với cả hai để đo khác biệt.
import type { Outcome, ScanId, ScanPolicy, Task } from "@scangrid/domain";

export type ApplyOutcomeResult =
  | { readonly kind: "duplicate" }                       // oracle 2: không đẩy wave hai lần
  | { readonly kind: "scan_missing" }                    // Redis mất trạng thái (Block 8, ADR-0002)
  | { readonly kind: "late"; readonly reason: string }   // B15: kết quả muộn sau khi đã chốt
  | { readonly kind: "progress"; readonly toDispatch: ReadonlyArray<Task> }
  | { readonly kind: "completed" };                      // verdict chốt đúng một lần

export interface ScanStateStore {
  /** Idempotent theo scanId. Trả về false nếu scan đã tồn tại. */
  createScan(scanId: ScanId, policy: ScanPolicy, firstStage: ReadonlyArray<Task>): Promise<boolean>;

  /** Đọc, gộp, tính stage, ghi lại: nguyên tử trong một script Lua. */
  applyOutcome(outcome: Outcome): Promise<ApplyOutcomeResult>;

  /** Đánh dấu task đã publish xong (sau RabbitMQ confirm). Hiểu rõ Q3. */
  markDispatched(scanId: ScanId, taskIds: ReadonlyArray<string>): Promise<void>;

  // TODO(Block 4): quét deadline (sorted set), lấy task "đã lên lịch" mà chưa "đã gửi",
  // progress không lùi (Q9), trần task mỗi scan (mục 8.7).
}
