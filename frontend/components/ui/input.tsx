import * as React from "react";

import { cn } from "@/lib/utils";

export const Input = React.forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(({ className, ...props }, ref) => (
  <input
    ref={ref}
    className={cn(
      "flex h-10 w-full rounded-xl border border-line bg-white px-3 py-2 text-sm text-ink outline-none placeholder:text-slate focus:border-ink",
      className,
    )}
    {...props}
  />
));

Input.displayName = "Input";
