// Ngôn ngữ chung (mục 8.10). Một khái niệm một tên, dùng chung cho code, log, dashboard, event.
// Đây là phác thảo; trạng thái scan đầy đủ (Block 4, "Hiểu rõ") là việc của bạn.

export type ScanId = string & { readonly __brand: "ScanId" };
export type ItemId = string & { readonly __brand: "ItemId" };
export type TaskId = string & { readonly __brand: "TaskId" };
export type TenantId = string & { readonly __brand: "TenantId" };

export type EngineRole =
  | "classifier"
  | "scanner"
  | "sanitizer"
  | "extractor"
  | "dlp"
  | "detonator";

export type OutcomeStatus =
  | "clean"
  | "suspicious"
  | "infected"
  | "error"
  | "resource_hazard";

/** Cấu hình hiệu lực của tenant cho một scan, chốt phiên bản lúc bắt đầu (mục 8.8). */
export interface ScanPolicy {
  readonly hash: string;
  readonly workflow: string;
  readonly workflowVersion: number;
  // TODO(Block 4, 7): timeout theo engine, danh sách engine, giới hạn archive, ...
}

/** Một lần chạy một engine trên một item: item × engine × attempt. */
export interface Task {
  readonly taskId: TaskId;
  readonly scanId: ScanId;
  readonly itemId: ItemId;
  readonly engine: string;
  readonly role: EngineRole;
  readonly attempt: number;
}

export interface Outcome {
  readonly taskId: TaskId;
  readonly scanId: ScanId;
  readonly itemId: ItemId;
  readonly engine: string;
  readonly attempt: number;
  readonly status: OutcomeStatus;
}

export type VerdictLevel = "clean" | "suspicious" | "infected" | "error";

export interface Verdict {
  readonly scanId: ScanId;
  readonly level: VerdictLevel;
  /** Engine trong danh sách mong đợi mà không có kết quả, kèm lý do (oracle 3). */
  readonly missing: ReadonlyArray<{ engine: string; itemId: ItemId; reason: "timeout" | "retry_exhausted" | "limit" }>;
}

/** Domain event (mục 8.10). Tên này chạy trên Kafka, trong log và dashboard. */
export type DomainEventName =
  | "ScanAccepted"
  | "ItemDiscovered"
  | "TaskDispatched"
  | "TaskStarted"
  | "TaskCompleted"
  | "TaskTimedOut"
  | "StageCompleted"
  | "ScanCompleted"
  | "VerdictDelivered";
