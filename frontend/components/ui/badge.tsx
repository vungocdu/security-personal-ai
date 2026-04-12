import { cva, type VariantProps } from "class-variance-authority";

import { cn } from "@/lib/utils";

const badgeVariants = cva("inline-flex items-center rounded-full px-2.5 py-1 text-[11px] font-medium tracking-wide", {
  variants: {
    variant: {
      default: "bg-mist text-ink",
      accent: "bg-accentSoft text-accent",
      success: "bg-[#E6F4EE] text-success",
      warning: "bg-[#FAEBDD] text-warning",
    },
  },
  defaultVariants: {
    variant: "default",
  },
});

export function Badge({ className, variant, ...props }: React.HTMLAttributes<HTMLDivElement> & VariantProps<typeof badgeVariants>) {
  return <div className={cn(badgeVariants({ variant }), className)} {...props} />;
}
