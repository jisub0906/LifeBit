package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ItemRepository extends JpaRepository<Item, Integer> {
    // JpaRepository를 상속받는 것만으로 기본적인 CRUD 메서드가 자동 생성됨
} 