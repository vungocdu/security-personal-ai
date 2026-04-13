import "@testing-library/jest-dom/vitest";

// Radix ScrollArea depends on ResizeObserver, which is not provided by jsdom.
class ResizeObserverMock {
  observe() {}
  unobserve() {}
  disconnect() {}
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
(globalThis as any).ResizeObserver = ResizeObserverMock;
