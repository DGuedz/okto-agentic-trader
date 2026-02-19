"use client";

import { useLanguage } from "@/components/LanguageProvider";

type LTextProps = {
  en: string;
  pt: string;
  className?: string;
};

export default function LText({ en, pt, className }: LTextProps) {
  const { language } = useLanguage();
  return <span className={className}>{language === "pt" ? pt : en}</span>;
}
