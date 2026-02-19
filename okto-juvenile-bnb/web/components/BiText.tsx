type BiTextProps = {
  en: string;
  pt: string;
  className?: string;
  enClassName?: string;
  ptClassName?: string;
};

export default function BiText({
  en,
  pt,
  className = "",
  enClassName = "",
  ptClassName = "",
}: BiTextProps) {
  return (
    <div className={className}>
      <div className={enClassName}>{en}</div>
      <div className={ptClassName}>{pt}</div>
    </div>
  );
}
