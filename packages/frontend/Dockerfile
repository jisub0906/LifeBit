# packages/frontend/Dockerfile

# 1. 빌드 환경 (Builder Stage)
FROM node:20-alpine AS builder
WORKDIR /app

# 모노레포 전체 컨텍스트 복사 (pnpm workspace 의존성 때문)
COPY . .

# 루트에서 pnpm 의존성 설치
RUN npm install -g pnpm && pnpm install && pnpm build

# 프론트엔드 프로젝트 빌드
RUN pnpm --filter frontend build


# 2. 프로덕션 환경 (Production Stage)
FROM nginx:stable-alpine
WORKDIR /usr/share/nginx/html

# Nginx 기본 설정 파일 삭제
RUN rm /etc/nginx/conf.d/default.conf

# 우리가 만든 Nginx 설정 파일 복사
COPY ./packages/frontend/nginx.conf /etc/nginx/conf.d/default.conf

# 빌드 스테이지에서 빌드된 결과물만 복사
COPY --from=builder /app/packages/frontend/dist .

# 80번 포트 노출
EXPOSE 80

# Nginx 실행
CMD ["nginx", "-g", "daemon off;"]

FROM node:20-alpine
WORKDIR /app
RUN npm install -g serve
COPY --from=builder /app/dist ./dist
EXPOSE 3000
CMD ["serve", "-s", "dist", "-l", "3000"]