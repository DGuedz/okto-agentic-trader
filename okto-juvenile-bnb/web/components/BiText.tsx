"use client";

import { useLanguage } from "@/components/LanguageProvider";

type BiTextProps = {
  en: string;
  pt: string;
  className?: string;
};

export default function BiText({
  en,
  pt,
  className = "",
}: BiTextProps) {
  const { language } = useLanguage();
  return <div className={className}>{language === "pt" ? pt : en}</div>;
}
