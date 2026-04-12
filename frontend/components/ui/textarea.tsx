import * as React from "react";

import { cn } from "@/lib/utils";

export const Textarea = React.forwardRef<HTMLTextAreaElement, React.TextareaHTMLAttributes<HTMLTextAreaElement>>(
  ({ className, ...props }, ref) => (
    <textarea
      ref={ref}
      className={cn(
        "flex min-h-[120px] w-full rounded-2xl border border-line bg-white px-3 py-3 text-sm text-ink outline-none placeholder:text-slate focus:border-ink",
        className,
      )}
      {...props}
    />
  ),
);

Textarea.displayName = "Textarea";
